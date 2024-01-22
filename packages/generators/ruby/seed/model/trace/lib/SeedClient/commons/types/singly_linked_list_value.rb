# frozen_string_literal: true

require_relative "commons/types/NodeId"
require "json"

module SeedClient
  module Commons
    class SinglyLinkedListValue
      attr_reader :head, :nodes, :additional_properties

      # @param head [Commons::NodeId]
      # @param nodes [Hash{Commons::NodeId => Commons::NodeId}]
      # @param additional_properties [OpenStruct] Additional properties unmapped to the current class definition
      # @return [Commons::SinglyLinkedListValue]
      def initialze(nodes:, head: nil, additional_properties: nil)
        # @type [Commons::NodeId]
        @head = head
        # @type [Hash{Commons::NodeId => Commons::NodeId}]
        @nodes = nodes
        # @type [OpenStruct] Additional properties unmapped to the current class definition
        @additional_properties = additional_properties
      end

      # Deserialize a JSON object to an instance of SinglyLinkedListValue
      #
      # @param json_object [JSON]
      # @return [Commons::SinglyLinkedListValue]
      def self.from_json(json_object:)
        struct = JSON.parse(json_object, object_class: OpenStruct)
        head Commons::NodeId.from_json(json_object: struct.head)
        nodes struct.nodes.transform_values do |v|
          Commons::NodeId.from_json(json_object: v)
        end
        new(head: head, nodes: nodes, additional_properties: struct)
      end

      # Serialize an instance of SinglyLinkedListValue to a JSON object
      #
      # @return [JSON]
      def to_json(*_args)
        { head: @head, nodes: @nodes.transform_values do |v|
                                Commons::NodeId.from_json(json_object: v)
                              end }.to_json
      end

      # Leveraged for Union-type generation, validate_raw attempts to parse the given hash and check each fields type against the current object's property definitions.
      #
      # @param obj [Object]
      # @return [Void]
      def self.validate_raw(obj:)
        obj.head.nil? || NodeId.validate_raw(obj: obj.head)
        obj.nodes.is_a?(Hash) != false || raise("Passed value for field obj.nodes is not the expected type, validation failed.")
      end
    end
  end
end